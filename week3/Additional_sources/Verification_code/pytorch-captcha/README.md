CNN Predict Verification Codes
=========

Get Started
====
- __Step 1： envr set up__

    Python2.7+ 、ImageCaptcha(pip install captcha)、 Pytorch(see: http://pytorch.org)


- __Step 2：gen verification codes__
    ```bash
    python captcha_gen.py
    ```
    run above codes, python will gen numbers of verification codes under  ./dataset/train/. You can control the number of imgs by change the count parameter in captcha-gen.py. More training imgs --> higher accuracy of the models 
    
- __Step 3：model training__
    ```bash
    python captcha_train.py
    ```
    will generate model.pkl

- __Step 4：test model__
    ```bash
    python captcha_test.py
    ```
    check accuracy

- __Step 5：predict using model__
    ```bash
    python captcha_predict.py
    ```
    