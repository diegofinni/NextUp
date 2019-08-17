import React, { Component } from 'react';
import { Card, Button, Icon, Label } from 'semantic-ui-react'
import axios from 'axios';
import { URL } from './config.js';


export class Song extends Component {
  constructor(props) {
    super(props);
    this.state = {
      votes: props.votes
    }

    this.vote = this.vote.bind(this)

  }

  vote() {
    this.setState({
      votes: this.state.votes + 1
    })

    console.log(this.props.songId)

    axios.get(`${URL}/vote`, {
      params: {
        song: this.props.songId
      },
    })
  }

  render() {
    return (
      <Card raised fluid >
        <Card.Content>
          <div>
          <Button as='div' labelPosition='right' floated='right'>
            <Button color='green' onClick={this.vote}>
              <Icon name='arrow up' color='black' />
              Vote
            </Button>
            <Label as='a' basic color='green' pointing='left'>
              {this.state.votes}
            </Label>
            </Button>
          </div>
          <Card.Header>{this.props.name}</Card.Header>
          <Card.Meta>{this.props.artist}</Card.Meta>

        </Card.Content>
      </Card>
    )
  }
}
