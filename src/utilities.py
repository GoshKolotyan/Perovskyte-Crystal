def set_train_opts(opt):
    if opt=="1var":
        train_cols = ["rC"]
        model_path="model/1var/"
    if opt=="2var":
        train_cols = ["zC", "rC"]
        model_path="model/2var/"
    if opt=="3var":
        train_cols = ["zC", "rC","TF"]
        model_path="model/3var/"
    if opt=="3var_noTF":
        train_cols = ["zC", "rC","rA"]
        model_path="model/3var_noTF/"
    if opt=="full":
        train_cols = ["xA", "yA", "zA", "xC", "yC", "zC", "rA", "rB", "rC", "TF"]
        model_path="model/full/"
    if opt=="full_clean":
        train_cols = ["xA", "yA", "zA", "xC", "yC", "zC", "rA", "rB", "rC", "TF"]
        model_path="model/full_clean/"
    data_path = "data/"
    return train_cols, model_path, data_path 