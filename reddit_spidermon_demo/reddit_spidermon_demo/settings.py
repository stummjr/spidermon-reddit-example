# -*- coding: utf-8 -*-

BOT_NAME = 'reddit_spidermon_demo'

SPIDER_MODULES = ['reddit_spidermon_demo.spiders']
NEWSPIDER_MODULE = 'reddit_spidermon_demo.spiders'

HTTPCACHE_ENABLED = True

# ---------------------------------------------------
# Validators
# ---------------------------------------------------
ITEM_PIPELINES = {
    'spidermon.contrib.scrapy.pipelines.ItemValidationPipeline': 800,
}

SPIDERMON_VALIDATION_MODELS = (
    'reddit_spidermon_demo.validators.NewsItem',
)

SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True
SPIDERMON_VALIDATION_ERRORS_FIELD = 'validation_error'
SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = True
# SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True

# ---------------------------------------------------
# Monitors
# ---------------------------------------------------
EXTENSIONS = {
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}

SPIDERMON_SPIDER_OPEN_MONITORS = (
    'reddit_spidermon_demo.monitors.SpiderOpenMonitorSuite',
)

SPIDERMON_SPIDER_CLOSE_MONITORS = (
    'reddit_spidermon_demo.monitors.SpiderCloseMonitorSuite',
)

# Slack
SPIDERMON_SLACK_SENDER_TOKEN = '<slack-api-token>'
SPIDERMON_SLACK_SENDER_NAME = 'bender'  # our slack bot :)
SPIDERMON_SLACK_RECIPIENTS = ['@you']
# SPIDERMON_SLACK_FAKE = True
