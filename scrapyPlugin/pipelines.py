
from scrapyPlugin.items import PhysicsSite

class PhysicsPipeline(object):

    def __init__(self, *args, **kwargs):
        # self.unique_id = unique_id
        self.items = []


    def process_item(self, item, spider):
        try:
            page = PhysicsSite.objects.get(article_link=item['article_link'])
            # Already exists, just update it
            instance = item.save(commit=False)
            instance.pk = page.pk
        except PhysicsSite.DoesNotExist:
            pass
        item.save()

        return item

