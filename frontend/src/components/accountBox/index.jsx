import React, { useState } from "react";
import styled from "styled-components";
import { LoginForm } from "./loginForm";
import { motion } from "framer-motion";
import { AccountContext } from "./accountContext"
import { SignupForm } from "./signupForm"

const BoxContainer = styled.div`
    width: 280px;
    height: 600px;
    display: flex;
    flex-direction: column;
    border-radius: 30px;
    background: #fff;
    box-shadow: 2px 2px 92px rgba(15, 15, 15, 0.28);
    position: relative;
    overflow: hidden;
    box-shadow: 5px, 5px, 2.5px rgba(15, 15, 15, 0.19);
    margin-top: 2%;
    margin-bottom: 2%;
`;

const TopContainer = styled.div`
    width: 100%;
    height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    padding: 50px 20px;
    background: #fff;
`;

const BackDrop = styled(motion.div)`
    width: 160%;
    height: 550px;
    position: absolute;
    display: flex;
    flex-direction: column;
    border-radius: 50%;
    transform: rotate(60deg);
    top: -300px;
    left: -80px;
    background: rgb(241, 196, 15);
    background: linear-gradient(
        58deg,
        rgba(241, 196, 15, 1) 60%,
        rgba(243, 172, 18, 1) 100%);
`;

const HeaderContainer = styled.div`
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: none;
`;

const HeaderText = styled.h2`
    font-size: 32px;
    font-weight: 500;
    line-height: 1.4;
    color: #fff;
    z-index: 10;
    margin: 0;
    background: none;
`;

const SamllText = styled.h3`
    color: #fff;
    font-weight: 500;
    font-size: 12px;
    z-index: 10;
    margin: 0;
    margin-top: 0px;
    background: none;
`;


const InnerContainer = styled.div`
    width:  100%;
    height: 90%;
    display:flex;
    flex-direction: column;
    padding: 0px 25px 5px;
    background: #fff;
`;

const backdropVariants = {
    expanded: {
        width: "233%",
        height: "1050px",
        borderRadius: "20%",
        transform: "rotate(60deg)"
    },
    collapsed: {
        width: "160%",
        height: "550px",
        borderRadius: "50%",
        transform: "rotate(60deg)"
    },
};

const expandingTransition = {
    type: "spring",
    duration: 2.3,
    stiffness: 35,
};

export function AccountBox(props) {
    const [isExpanded, setExpanded] = useState(false);
    const [active, setActive] = useState("signin");

    const playExpandingAnimation = () => {
        setExpanded(true);
        setTimeout(() => {
            setExpanded(false);
        }, expandingTransition.duration * 1000 - 1500);
    };

    const switchToSignup = () => {
        playExpandingAnimation();
        setTimeout(() => {
            setActive("signup");
        }, 400);
    };

    const switchToSignin = () => {
        playExpandingAnimation();
        setTimeout(() => {
            setActive("signin");
        }, 400);
    };

    const contextValue = { switchToSignup, switchToSignin };

    return (
        <AccountContext.Provider value={contextValue}>
            <BoxContainer>
                <TopContainer>
                    <BackDrop
                        initial={false}
                        animate={isExpanded ? "expanded" : "collapsed"}
                        variants={backdropVariants}
                        transition={expandingTransition}
                    />
                    {active === "signin" && <HeaderContainer>
                        <HeaderText>Welcome</HeaderText>
                        <HeaderText>Back</HeaderText>
                        <SamllText>Please Sign-in to continue!</SamllText>
                    </HeaderContainer>}
                    {active === "signup" && <HeaderContainer>
                        <HeaderText>Create</HeaderText>
                        <HeaderText>Acoount</HeaderText>
                        <SamllText>Please Sign-up to continue!</SamllText>
                    </HeaderContainer>}
                </TopContainer>
                <InnerContainer>
                    {active === "signin" && <LoginForm />}
                    {active === "signup" && <SignupForm />}
                </InnerContainer>
            </BoxContainer>
        </AccountContext.Provider>
    );
}