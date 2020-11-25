import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../components/Main'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Main',
        component: Main
    },
    {
        path: '/scanner',
        name: 'QRScanner',
        component: () => import(/* webpackChunkName: "about" */ '../components/QRScanner')
    },
    {
        path: '/registrant',
        name: 'RegistrantList',
        component: () => import(/* webpackChunkName: "about" */ '../components/RegistrantList')
    },
    {
        path: '/opening',
        name: 'OpeningCount',
        component: () => import(/* webpackChunkName: "about" */ '../components/OpeningCount')
    },
    {
        path: '/registrant-table',
        name: 'RegistrantTable',
        component: () => import(/* webpackChunkName: "about" */ '../components/RegistrantTable')
    },
    {
        path: '/program',
        name: 'Program',
        component: () => import(/* webpackChunkName: "about" */ '../components/Program')
    },
    {
        path: '/program-admin',
        name: 'ProgramAdmin',
        component: () => import(/* webpackChunkName: "about" */ '../components/ProgramAdmin')
    },
    {
        path: '/program-admin/:programId/edit',
        name: 'ProgramAdminEdit',
        component: () => import(/* webpackChunkName: "about" */ '../components/ProgramAdmin')
    },
    {
        path: '/users/:userNumber/detail',
        name: 'UserDetail',
        component: () => import(/* webpackChunkName: "about" */ '../components/UserDetail')
    },
    {
        path: '/register/add',
        name: 'RegisterAdd',
        component: () => import(/* webpackChunkName: "about" */ '../components/RegisterAdd')
    },
    {
        path: '/Gallery/add',
        name: 'Gallery',
        component: () => import(/* webpackChunkName: "about" */ '../components/GalleryAdmin')
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router