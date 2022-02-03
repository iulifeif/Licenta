import React, { useContext } from "react";
import { BoxContainer, FormContainer, Input, MutedLink, SubmitButton, BoldLink, BottomForm } from "./common"
import { AccountContext } from "./accountContext";

export function LoginForm(props) {
    const { switchToSignup } = useContext(AccountContext);

    return (
        <BoxContainer>
            <FormContainer>
                <Input type="email" placeholder="Email" />
                <Input type="password" placeholder="Password" />
                <MutedLink href="#">Forget your password?</MutedLink>
            </FormContainer>
            <BottomForm>
                <SubmitButton type="submit">Sign In</SubmitButton>
                <MutedLink href="#">
                    Don't have an account?
                    <BoldLink href="#" onClick={switchToSignup}>
                        Signup
                    </BoldLink>
                </MutedLink>
            </BottomForm>
        </BoxContainer>
    );
}