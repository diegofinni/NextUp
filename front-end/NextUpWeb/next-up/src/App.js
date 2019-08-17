import React, { Component } from 'react';
import { Song } from './Song.js';
import { Header, Divider, Icon, Segment } from 'semantic-ui-react'
import axios from 'axios';
import { URL } from './config.js'
import './App.css';

class App extends Component {
  constructor(props) {
    super(props)

    this.state = {}
    this.getData()
  }

  getData() {
    axios.get(`${URL}/songs/votes`)
      .then(({data}) => {
        this.setState(data)
      })
  }

  render() {
    const songs = Object.values(this.state).map(data => {
      const {id, votes, artist, name} = data
      return (<Song key={id} songId={id} name={name} artist={artist} votes={votes} />)
    })

    return (
      <Segment inverted>
        <div class= 'inverted'>
          <div></div>
          <Header as='h2' icon textAlign='center' color='green'>
            <Icon name='angle double up' circular />
            <Header.Content>Next Up</Header.Content>
          </Header>
          {songs}
        </div>
      </Segment>
    );
  }
}

export default App;
