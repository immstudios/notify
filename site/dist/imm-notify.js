(function (window, document, undefined) {
    "use strict";
    if (window.immNotify) {
        return;
    }

    var immNotify = function(channel, handler) {
            this.channel = channel;
            this.handler = handler;
            this.connect();
        } // Notify.constructor

    immNotify.prototype.connect = function() {
            var handler = this.handler;
            this.socket = new WebSocket("wss://notify.immstudios.org/ws/" + this.channel);
            this.socket.onmessage = function(event){
                var message = JSON.parse(event.data);
                handler(message);
            };
        } // Notify.connect

    window.immNotify = immNotify;
})(window, document);
