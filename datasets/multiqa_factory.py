

class MultiQAFactory:
    def __init__(self):
        pass

    def build_dataset(self, dastaset_name, split, preprocessor, sample_size):


        mod = __import__('datasets.' + dastaset_name + '.' + dastaset_name.lower(), fromlist=[dastaset_name])
        dataset_class = getattr(mod, dastaset_name)()

        contexts = dataset_class.build_contexts(split, preprocessor, sample_size)
        header = dataset_class.build_header(contexts, split, preprocessor)

        return header, contexts

    def format_predictions(self, dastaset_name, predictions):

        mod = __import__('datasets.' + dastaset_name + '.' + dastaset_name.lower(), fromlist=[dastaset_name])
        dataset_class = getattr(mod, dastaset_name)()

        predictions = dataset_class.format_predictions(predictions)

        return predictions



