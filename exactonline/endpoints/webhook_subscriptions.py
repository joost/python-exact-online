from .base import APIEndpointWithDivision

from exactonline.models.webhook_subscriptions import WebhookSubscription, WebhookSubscriptionList

class WebhookSubscriptionMethods(APIEndpointWithDivision):

    def __init__(self, api):
        super().__init__(api, 'webhooks/WebhookSubscriptions', WebhookSubscription, WebhookSubscriptionList)