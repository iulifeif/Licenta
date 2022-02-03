import styled from "styled-components";
import { AccountBox } from "./components/accountBox";
import { HomePage } from "./components/home/index.jsx"

const AppContainer = styled.div `
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

function App() {
    return ( <AppContainer>
        <AccountBox/>
        </AppContainer>
    );
};

export default App;
