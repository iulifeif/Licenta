import React, { useContext } from "react";
import { BoxContainer, FormContainer, Input, MutedLink, SubmitButton, BoldLink } from "./common"
import { Marginer } from "../marginer";
import { AccountContext } from "./accountContext";

export function LoginForm(props) {
    const { switchToSignup } = useContext(AccountContext);

    return (
        <BoxContainer>
            <FormContainer>
                <Input type="email" placeholder="Email" />
                <Input type="password" placeholder="Password" />
            </FormContainer>
            <Marginer direction="vertical" margin={10} />
            <MutedLink href="#">Forget your password?</MutedLink>
            <Marginer direction="vertical" margin="1.4em" />
            <SubmitButton type="submit">Sign In</SubmitButton>
            <Marginer direction="vertical" margin="1.4em" />
            <MutedLink href="#">
                Don't have an account? 
                <BoldLink href="#" onClick={switchToSignup}>
                    Signup
                </BoldLink>
            </MutedLink>
        </BoxContainer>
    );
}