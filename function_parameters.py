
class WritePaths:
    def __init__(self, w_suffix: str):
        self.predicted_data_path = f'metrics/predicted_data_{w_suffix}.csv'
        self.auc_image_path = f'models/model{clf_suffix}{w_suffix}.joblib.dat'
        self.confusion_matrix_path = f'models/pipeline{clf_suffix}{w_suffix}.joblib.dat'
        self.roc_curve_path = f'models/pipeline{clf_suffix}{w_suffix}.joblib.dat'
        self.output_path_5 = f'models/pipeline{clf_suffix}{w_suffix}.joblib.dat'
        self.output_path_6 = f'models/pipeline{clf_suffix}{w_suffix}.joblib.dat'

write_path = WritePaths('xgb_model')

def save_model_performance(write_path):
    # We can acces to paths this way:
    write_path.predicted_data_path

