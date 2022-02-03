import React from "react";
import styled from "styled-components";
import logo from "../../assets/logo.png"
import { SubmitButton } from "../accountBox/common";
import { AccountBox } from "../accountBox/index";
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';

const FirstPage = styled.div`
    width: 40%;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    background: none;
`;

const LogoImg = styled.img.attrs({
    src: `${logo}`
})`
    width: 500px;
    height: 500px;
    margin: 15px;
    background: none;
`;

const FirstText = styled.h2`
    font-size: 30px;
    font-weight: 600;
    line-height: 1.24;
    color: #fff;
    z-index: 10;
    margin: 0;
    background: none;
`;

export function HomePage(props) {
    return (
        <Router>

            <FirstPage>
                <LogoImg />
                <FirstText> Învață mai bine Limba Română! </FirstText>
                <SubmitButton type="submit" component={AccountBox}>
                    <Link to="/login">
                        START
                    </Link>
                </SubmitButton>
            </FirstPage>
            {/* <Switch>
                <Route exact path="/login" component={AccountBox} />
            </Switch> */}
        </Router>
    );
};