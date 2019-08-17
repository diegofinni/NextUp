import React, { Component } from 'react';
import { Button, Progress } from 'semantic-ui-react'


export class Mae extends Component {
  constructor(props) {
    super(props);
    this.state = {
      favoriteFood: props.favoriteFood,
      num: 0
    }

    this.incrementCounter = this.incrementCounter.bind(this)
  }

  incrementCounter() {
    this.setState({
      num: this.state.num + 1
    })
  }

  render() {
    return (
      <div>
        <b>Mae</b> likes <i>{this.state.favoriteFood}</i>

        <Button onClick={this.incrementCounter}>
          Click me for {this.state.favoriteFood}
        </Button>

        <br />
        <Progress percent={this.state.num} indicating />
        We've counted {this.state.num} clicks
      </div>
    )
  }
}
