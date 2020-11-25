import firebase from "firebase/app";
import 'firebase/auth'
import 'firebase/firestore'

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyCqoGkV3iNOAyvhWm3TCgoONU9Lza6hBL8",
    authDomain: "la-forum-2020.firebaseapp.com",
    databaseURL: "https://la-forum-2020.firebaseio.com",
    projectId: "la-forum-2020",
    storageBucket: "la-forum-2020.appspot.com",
    messagingSenderId: "166041537934",
    appId: "1:166041537934:web:c1967c8278b7de4020a8df",
    measurementId: "G-1EFPJEV2P3"
};

firebase.initializeApp(firebaseConfig)

const db = firebase.firestore()
const users = db.collection('users')
const programs = db.collection('programs')
const draws = db.collection('draws')
const galleries = db.collection('galleries')
const registers = db.collection('registers')
const checkins = db.collection('checkins')

export {
    firebase as fb,
    db,
    users,
    programs,
    draws,
    galleries,
    registers,
    checkins
};