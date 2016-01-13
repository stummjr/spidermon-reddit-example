from spidermon import Monitor, MonitorSuite, monitors
from spidermon.contrib.monitors.mixins import (
    StatsMonitorMixin, JobMonitorMixin
)
from spidermon.contrib.actions.slack.notifiers import (
    SendSlackMessageSpiderStarted, SendSlackMessageSpiderFinished
)


@monitors.name('Item count')
class ItemCountMonitor(Monitor, StatsMonitorMixin, JobMonitorMixin):
    @monitors.name('Minimum number of items')
    def test_minimum_number_of_items(self):
        expected = 25
        msg = 'Number of scraped items is different of %d' % expected
        self.assertEqual(self.item_scraped_count(), expected, msg=msg)

    def item_scraped_count(self):
        return getattr(self.stats, 'item_scraped_count', 0)


class SpiderOpenMonitorSuite(MonitorSuite):
    monitors_finished_actions = [
        SendSlackMessageSpiderStarted,
    ]


class SpiderCloseMonitorSuite(MonitorSuite):
    monitors = [
        ItemCountMonitor,
    ]
    monitors_finished_actions = [
        SendSlackMessageSpiderFinished,
    ]
