import React from 'react';

import '../styles/Time.css';

class Time extends React.Component {
  constructor(props) {
    super(props);
    const date = new Date();
    this.state = {
      hours: date.getHours(),
      minutes: date.getMinutes(),
      seconds: date.getSeconds()
    };
  }

  getNow() {
    const date = new Date();
    this.setState(state => ({
      hours: date.getHours(),
      minutes: ((date.getMinutes() < 10)? ' 0': ' ') + date.getMinutes(),
      seconds: ((date.getSeconds() < 10)? ' 0': ' ') + date.getSeconds()
    }))
  }

  componentDidMount() {
    this.interval = setInterval(() => this.getNow(), 1000);
  }

  render() {
    return (
      <div className="Time">
      {this.state.hours} :
      {this.state.minutes} :
      {this.state.seconds}
      </div>
    )
  }
}

export default Time;
