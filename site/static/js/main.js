requirejs.config({
    appDir: ".",
    baseUrl: "js",
    paths: {
        'jquery': ['/static/js/jquery.min'],
        'bootstrap': ['/static/js/bootstrap.min'],
        'imm-notify': ['/dist/imm-notify.min']
    },
    shim: {
        'bootstrap' : ['jquery']
    }
});

require(['jquery', 'bootstrap', 'imm-notify'], function($) {

    function notify_handler(data){
        $("#messaging").html(data);
    }

    notify = new immNotify("demo", notify_handler);
});
