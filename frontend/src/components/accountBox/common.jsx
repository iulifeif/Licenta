import styled from "styled-components";


export const BoxContainer = styled.div`
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content:space-around;
    margin-top: 10px;
    background: #fff;
`;

export const FormContainer = styled.form`
    width: 100%;
    display: flex;
    flex-direction: column;
    box-shadow: 0px, 0px, 10px rgba(15, 15, 15, 0.19);
`;

export const MutedLink = styled.a`
    font-size: 12px;
    color: black;
    font-weight: 500;
    text-decoration: none;
    background: none;
`;

export const BoldLink = styled.a`
    font-size: 12px;
    color: rgb(182, 147, 7);
    font-weight: 500;
    text-decoration: none;
    margin: 0 4px;
    background: none;
`;

export const Input = styled.input`
    width: 100%;
    height:42px;
    outline: none;
    border: 0px solid black;
    padding: 0px 10px;
    border-bottom: 1.5px solid rgba(44, 44, 44, 0.253);
    transition: all 200ms ease-in-out;
    font-size: 13px;

    &::placeholder{
        color: #000000;
    }
    /* &:not(:last-of-type){
        border-bottom: 1.5px solid rgba(200, 200, 200, 0.4)
    } */
    &:focus{
        outline: none;
        border-bottom: 2px solid rgb(241, 196, 15);
    }
    background: #fff;
`;

export const SubmitButton = styled.button`
    width: 60%;
    padding: 10px 15%;
    color: #fff;
    font-size: 15px;
    font-weight: 800;
    border: none;
    border-radius: 100px 100px 100px 100px;
    cursor: pointer;
    transition: all, 240ms ease-in-out;
    background: rgb(241, 196, 15);
    background: linear-gradient(
        58deg,
        rgba(241, 196, 15, 1) 60%,
        rgba(243, 172, 18, 1) 100%);
    &:hover {
        filter: brightness(1.1);
    }
`;