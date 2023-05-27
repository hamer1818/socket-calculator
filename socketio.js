const { io } =require ("socket.io-client");

// FastAPI servise bağlanmak için açağıdaki satır aktif olmalı
const socket = io("http://127.0.0.1:8081",{transports: ["websocket", "polling", "flashsocket"] ,path:"/ws/socket.io"});

// Nodejs de yazılmış socket bağlantısı için aşağıdaki kod aktif olmalı
//const socket = io("http://localhost:8081",{transports: ["websocket", "polling", "flashsocket"] });

/*
socket.on("connect", () => { console.log("Connected", socket.id) }); 
socket.on("response", () => { console.log("Response", socket.id) });  
socket.on("message", data => { console.log(data) });*/

// socket.on("Ne Alirsiniz", data => { console.log(data) });

const renk1 = "\033[93m";
const renk2 = "\033[94m";
const renk3 = "\033[92m";
const renk4 = "\033[96m";

socket.on("bol",data=> { 
    console.log(renk1+"Bölümden sonuç: "+data) 
});

socket.on("toplam",data=> {
    console.log(renk2+"Toplamadan sonuç: "+data)
});

socket.on("carp",data=> {
    console.log(renk3+"Çarpımdan sonuç: "+data)
});

socket.on("cikar",data=> {
    console.log(renk4+"Çıkarmadan sonuç: "+data)
});

// socket.emit("mesaj1", "Merhaba");

console.log("Hesap makinesi aktif");