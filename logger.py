import logging

root_logger = logging.getLogger().setLevel(logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
root_logger.addHandler(console)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.StreamHandler().setLevel(logging.INFO)])