{"filter":false,"title":"settings.py","tooltip":"/carolscakes/settings.py","undoManager":{"mark":73,"position":73,"stack":[[{"start":{"row":27,"column":17},"end":{"row":27,"column":86},"action":"insert","lines":["'458124f84c284413a9df9364028ec6e4.vfs.cloud9.us-east-1.amazonaws.com'"],"id":2}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":65},"action":"remove","lines":["'4#!gc!btxqbyf-+95vu18&3%oe6wgelvctsva((h!&mo!hr6@b'"],"id":3},{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["o"]},{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["."],"id":4},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["e"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":18},"action":"remove","lines":["en"],"id":5},{"start":{"row":22,"column":16},"end":{"row":22,"column":23},"action":"insert","lines":["environ"]}],[{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["."],"id":6},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["g"]}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"remove","lines":["g"],"id":7},{"start":{"row":22,"column":24},"end":{"row":22,"column":29},"action":"insert","lines":["get()"]}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":30},"action":"insert","lines":["''"],"id":8}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["S"],"id":9},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["E"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["C"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["R"]}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":33},"action":"remove","lines":["SECR"],"id":10},{"start":{"row":22,"column":29},"end":{"row":22,"column":39},"action":"insert","lines":["SECRET_KEY"]}],[{"start":{"row":22,"column":41},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":6},"action":"insert","lines":["''"],"id":14}],[{"start":{"row":39,"column":5},"end":{"row":39,"column":6},"action":"insert","lines":["c"],"id":15},{"start":{"row":39,"column":6},"end":{"row":39,"column":7},"action":"insert","lines":["a"]},{"start":{"row":39,"column":7},"end":{"row":39,"column":8},"action":"insert","lines":["k"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["e"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["s"]}],[{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":[","],"id":16}],[{"start":{"row":57,"column":8},"end":{"row":57,"column":19},"action":"remove","lines":["'DIRS': [],"],"id":18},{"start":{"row":57,"column":8},"end":{"row":57,"column":53},"action":"insert","lines":["'DIRS': [os.path.join(BASE_DIR,'templates')],"]}],[{"start":{"row":39,"column":12},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":6},"action":"insert","lines":["''"],"id":20}],[{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["p"],"id":21},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["r"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["o"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["d"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["u"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["c"]},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["t"]},{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":[","],"id":22}],[{"start":{"row":118,"column":0},"end":{"row":122,"column":0},"action":"remove","lines":["# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'",""],"id":23},{"start":{"row":118,"column":0},"end":{"row":140,"column":42},"action":"insert","lines":["# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )","STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')","","MESSAGE_STORAGE = \"django.contrib.messages.storage.session.SessionStorage\"","","# Password re-set email access","EMAIL_USE_TLS = True","EMAIL_HOST = 'smtp.gmail.com'","EMAIL_HOST_USER = os.environ.get(\"EMAIL_ADDRESS\")","EMAIL_HOST_PASSWORD = os.environ.get(\"EMAIL_PASSWORD\")","EMAIL_PORT = 587","","# Media access","MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","","# Stripe Access","STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')","STRIPE_SECRET = os.getenv('STRIPE_SECRET')"]}],[{"start":{"row":40,"column":15},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":41,"column":4},"end":{"row":41,"column":6},"action":"insert","lines":["''"],"id":25}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":6},"action":"insert","lines":["c"],"id":26},{"start":{"row":41,"column":6},"end":{"row":41,"column":7},"action":"insert","lines":["a"]},{"start":{"row":41,"column":7},"end":{"row":41,"column":8},"action":"insert","lines":["r"]},{"start":{"row":41,"column":8},"end":{"row":41,"column":9},"action":"insert","lines":["o"]},{"start":{"row":41,"column":9},"end":{"row":41,"column":10},"action":"insert","lines":["l"]}],[{"start":{"row":41,"column":5},"end":{"row":41,"column":10},"action":"remove","lines":["carol"],"id":27},{"start":{"row":41,"column":5},"end":{"row":41,"column":16},"action":"insert","lines":["carolscakes"]}],[{"start":{"row":41,"column":17},"end":{"row":41,"column":18},"action":"insert","lines":[","],"id":28}],[{"start":{"row":121,"column":0},"end":{"row":122,"column":0},"action":"insert","lines":["",""],"id":29}],[{"start":{"row":122,"column":0},"end":{"row":124,"column":0},"action":"insert","lines":["STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )",""],"id":30}],[{"start":{"row":124,"column":0},"end":{"row":126,"column":55},"action":"remove","lines":["","STATIC_URL = '/static/'","STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )"],"id":31},{"start":{"row":123,"column":55},"end":{"row":124,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":136,"column":0},"end":{"row":137,"column":44},"action":"remove","lines":["MEDIA_URL = '/media/'","MEDIA_ROOT = os.path.join(BASE_DIR, 'media')"],"id":32},{"start":{"row":136,"column":0},"end":{"row":137,"column":21},"action":"insert","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'"]}],[{"start":{"row":41,"column":18},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":6},"action":"insert","lines":["''"],"id":36}],[{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["a"],"id":37},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["c"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["c"]},{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["o"]},{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":["u"]},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["n"]},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["t"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":[","],"id":38}],[{"start":{"row":38,"column":33},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":29},"action":"insert","lines":["'django_forms_bootstrap',"],"id":40}],[{"start":{"row":106,"column":0},"end":{"row":107,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":106,"column":0},"end":{"row":109,"column":1},"action":"insert","lines":["AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.CaseInsensitiveAuth'","]"],"id":42}],[{"start":{"row":109,"column":1},"end":{"row":110,"column":0},"action":"remove","lines":["",""],"id":43}],[{"start":{"row":139,"column":16},"end":{"row":140,"column":0},"action":"insert","lines":["",""],"id":44}],[{"start":{"row":140,"column":0},"end":{"row":140,"column":36},"action":"insert","lines":["DEFAULT_FROM_EMAIL = EMAIL_HOST_USER"],"id":45}],[{"start":{"row":140,"column":0},"end":{"row":140,"column":36},"action":"remove","lines":["DEFAULT_FROM_EMAIL = EMAIL_HOST_USER"],"id":46}],[{"start":{"row":137,"column":47},"end":{"row":137,"column":48},"action":"remove","lines":["\""],"id":65}],[{"start":{"row":137,"column":47},"end":{"row":137,"column":48},"action":"insert","lines":["'"],"id":66}],[{"start":{"row":137,"column":33},"end":{"row":137,"column":34},"action":"remove","lines":["\""],"id":67}],[{"start":{"row":137,"column":33},"end":{"row":137,"column":34},"action":"insert","lines":["'"],"id":68}],[{"start":{"row":138,"column":37},"end":{"row":138,"column":38},"action":"remove","lines":["\""],"id":69}],[{"start":{"row":138,"column":37},"end":{"row":138,"column":38},"action":"insert","lines":["'"],"id":70}],[{"start":{"row":138,"column":52},"end":{"row":138,"column":53},"action":"remove","lines":["\""],"id":71}],[{"start":{"row":138,"column":52},"end":{"row":138,"column":53},"action":"insert","lines":["'"],"id":72}],[{"start":{"row":68,"column":70},"end":{"row":69,"column":0},"action":"insert","lines":["",""],"id":73},{"start":{"row":69,"column":0},"end":{"row":69,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":69,"column":16},"end":{"row":69,"column":59},"action":"insert","lines":["'django.template.context_processors.debug',"],"id":74}],[{"start":{"row":69,"column":57},"end":{"row":69,"column":58},"action":"remove","lines":["'"],"id":75},{"start":{"row":69,"column":56},"end":{"row":69,"column":57},"action":"remove","lines":["g"]},{"start":{"row":69,"column":55},"end":{"row":69,"column":56},"action":"remove","lines":["u"]},{"start":{"row":69,"column":54},"end":{"row":69,"column":55},"action":"remove","lines":["b"]},{"start":{"row":69,"column":53},"end":{"row":69,"column":54},"action":"remove","lines":["e"]},{"start":{"row":69,"column":52},"end":{"row":69,"column":53},"action":"remove","lines":["d"]}],[{"start":{"row":69,"column":52},"end":{"row":69,"column":53},"action":"insert","lines":["m"],"id":76},{"start":{"row":69,"column":53},"end":{"row":69,"column":54},"action":"insert","lines":["e"]},{"start":{"row":69,"column":54},"end":{"row":69,"column":55},"action":"insert","lines":["d"]},{"start":{"row":69,"column":55},"end":{"row":69,"column":56},"action":"insert","lines":["i"]},{"start":{"row":69,"column":56},"end":{"row":69,"column":57},"action":"insert","lines":["a"]},{"start":{"row":69,"column":57},"end":{"row":69,"column":58},"action":"insert","lines":["'"]}],[{"start":{"row":69,"column":16},"end":{"row":69,"column":59},"action":"remove","lines":["'django.template.context_processors.media',"],"id":77},{"start":{"row":69,"column":16},"end":{"row":70,"column":46},"action":"insert","lines":["'django.template.context_processors.media',","                'cart.contexts.cart_contents',"]}],[{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"remove","lines":[","],"id":79},{"start":{"row":43,"column":14},"end":{"row":44,"column":0},"action":"insert","lines":["",""]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":44,"column":4},"end":{"row":44,"column":6},"action":"insert","lines":["''"],"id":80}],[{"start":{"row":44,"column":5},"end":{"row":44,"column":6},"action":"insert","lines":["c"],"id":81},{"start":{"row":44,"column":6},"end":{"row":44,"column":7},"action":"insert","lines":["a"]},{"start":{"row":44,"column":7},"end":{"row":44,"column":8},"action":"insert","lines":["r"]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":[","],"id":82}],[{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":[","],"id":83}],[{"start":{"row":44,"column":11},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":84},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":45,"column":4},"end":{"row":45,"column":6},"action":"insert","lines":["''"],"id":85}],[{"start":{"row":45,"column":5},"end":{"row":45,"column":6},"action":"insert","lines":["e"],"id":86},{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"insert","lines":["c"]}],[{"start":{"row":45,"column":5},"end":{"row":45,"column":7},"action":"remove","lines":["ec"],"id":87},{"start":{"row":45,"column":5},"end":{"row":45,"column":14},"action":"insert","lines":["ecommerce"]}],[{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":[","],"id":88}],[{"start":{"row":45,"column":16},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":89},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":6},"action":"insert","lines":["''"],"id":90}],[{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"insert","lines":["c"],"id":91},{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["h"]},{"start":{"row":46,"column":7},"end":{"row":46,"column":8},"action":"insert","lines":["e"]},{"start":{"row":46,"column":8},"end":{"row":46,"column":9},"action":"insert","lines":["c"]},{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"insert","lines":["k"]},{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"insert","lines":["o"]},{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"insert","lines":["u"]}],[{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"insert","lines":["t"],"id":92}],[{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"insert","lines":[","],"id":93}],[{"start":{"row":46,"column":15},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":94},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":6},"action":"insert","lines":["''"],"id":95}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["s"],"id":96},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["e"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["a"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["r"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["c"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["h"]}],[{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":[","],"id":97}]]},"ace":{"folds":[],"scrolltop":1538,"scrollleft":0,"selection":{"start":{"row":154,"column":42},"end":{"row":154,"column":42},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":50,"state":"start","mode":"ace/mode/python"}},"timestamp":1565994002664,"hash":"23b352e250403bb4cca214adfbaba4ba0ff3072d"}