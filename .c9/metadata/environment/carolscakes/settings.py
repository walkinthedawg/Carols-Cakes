{"filter":false,"title":"settings.py","tooltip":"/carolscakes/settings.py","undoManager":{"mark":29,"position":29,"stack":[[{"start":{"row":27,"column":17},"end":{"row":27,"column":86},"action":"insert","lines":["'458124f84c284413a9df9364028ec6e4.vfs.cloud9.us-east-1.amazonaws.com'"],"id":2}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":65},"action":"remove","lines":["'4#!gc!btxqbyf-+95vu18&3%oe6wgelvctsva((h!&mo!hr6@b'"],"id":3},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["o"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["."],"id":4},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["e"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":18},"action":"remove","lines":["en"],"id":5},{"start":{"row":22,"column":16},"end":{"row":22,"column":23},"action":"insert","lines":["environ"]}],[{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["."],"id":6},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["g"]}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"remove","lines":["g"],"id":7},{"start":{"row":22,"column":24},"end":{"row":22,"column":29},"action":"insert","lines":["get()"]}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":30},"action":"insert","lines":["''"],"id":8}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["S"],"id":9},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["E"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["C"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["R"]}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":33},"action":"remove","lines":["SECR"],"id":10},{"start":{"row":22,"column":29},"end":{"row":22,"column":39},"action":"insert","lines":["SECRET_KEY"]}],[{"start":{"row":22,"column":41},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["''"],"id":14}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["c"],"id":15},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["a"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["k"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["e"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":[","],"id":16}],[{"start":{"row":57,"column":8},"end":{"row":57,"column":19},"action":"remove","lines":["'DIRS': [],"],"id":18},{"start":{"row":57,"column":8},"end":{"row":57,"column":53},"action":"insert","lines":["'DIRS': [os.path.join(BASE_DIR,'templates')],"]}],[{"start":{"row":39,"column":12},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["''"],"id":20}],[{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["p"],"id":21},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["r"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["o"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["d"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["u"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["c"]},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["t"]},{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":[","],"id":22}],[{"start":{"row":118,"column":0},"end":{"row":122,"column":0},"action":"remove","lines":["# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'",""],"id":23},{"start":{"row":118,"column":0},"end":{"row":140,"column":42},"action":"insert","lines":["# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')","","MESSAGE_STORAGE = \"django.contrib.messages.storage.session.SessionStorage\"","","# Password re-set email access","EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","EMAIL_PORT = 587","","# Media access","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","","# Stripe Access","STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')","STRIPE_SECRET = os.getenv('STRIPE_SECRET')"]}],[{"start":{"row":40,"column":15},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":6},"action":"insert","lines":["''"],"id":25}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["c"],"id":26},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["a"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["r"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["o"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":10},"action":"remove","lines":["carol"],"id":27},{"start":{"row":41,"column":5},"end":{"row":41,"column":16},"action":"insert","lines":["carolscakes"]}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":[","],"id":28}],[{"start":{"row":121,"column":0},"end":{"row":122,"column":0},"action":"insert","lines":["",""],"id":29}],[{"start":{"row":122,"column":0},"end":{"row":124,"column":0},"action":"insert","lines":["STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )",""],"id":30}],[{"start":{"row":124,"column":0},"end":{"row":126,"column":55},"action":"remove","lines":["","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )"],"id":31},{"start":{"row":123,"column":55},"end":{"row":124,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":136,"column":0},"end":{"row":137,"column":44},"action":"remove","lines":["MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":32},{"start":{"row":136,"column":0},"end":{"row":137,"column":21},"action":"insert","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'"]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "],"id":34},{"start":{"row":39,"column":12},"end":{"row":40,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":15},"action":"remove","lines":["'products',"],"id":33}]]},"ace":{"folds":[],"scrolltop":351,"scrollleft":0,"selection":{"start":{"row":36,"column":22},"end":{"row":36,"column":22},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565318887104,"hash":"65c16a808f8670f46dfdc0ac714ef641546409ad"}