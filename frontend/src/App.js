import React from "react";
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/AutorList';
import UserList from "./components/UserList";
import Menu from "./components/menu";
import Footer from "./components/footer";
import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'users': []
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/authors/')
            .then( response => {
                const authors = response.data

                this.setState({
                    'authors': authors,
                })
            })
            .catch(error => console.log(error))

        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then( response => {
                const users = response.data

                this.setState({
                    'users': users,
                })
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <Menu />
                <AuthorList authors={this.state.authors} />
                <br/>
                <UserList users={this.state.users} />
                <Footer />
            </div>

        )
    }
}

export default App;
