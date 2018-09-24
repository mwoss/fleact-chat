import React from "react";
import {Route, Switch} from "react-router-dom"

import LogInPage from "./auth/LogInPage";
import HomePage from "./user/HomePage";
import Chat from "./app/Chat";

const App = () => (
    <main>
        <Switch>
            <Route exact path='/' component={HomePage}/>
            <Route path='/login' compontent={LogInPage}/>
            <Route path='/chatroom/:name' component={Chat}/>
        </Switch>
    </main>
);

export default App