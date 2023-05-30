import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons';

import { useState } from 'react';

import './Block.css';

const CustomSlider = (props) => {

  const { data } = props;

  const [offsetX, setOffsetX] = useState(-100);

  function pgLeft() {
    if(offsetX >= -100){
    	setOffsetX(offsetX => -100);
    }else{
    	setOffsetX(offsetX => offsetX + 100);
    }
  }

  function pgRight() {
  	var pageLimit = (data.texts.length*-100);
    if(offsetX <= pageLimit){
    	setOffsetX(offsetX => pageLimit);
    }else{
    	setOffsetX(offsetX => offsetX - 100);
    }
  }

  return (
    <div style={{ display: 'flex' }}>
      <span className="cslider-arrow-left" onClick={pgLeft}>
        <FontAwesomeIcon icon={faArrowLeft} />
      </span>
      <div className="component-cslider cslider-view">
        <div
          key={0}
          style={{ marginLeft: offsetX + '%' }}
          className="cslider-item"
        ></div>
        {data.texts &&
          data.texts.map((text, index) => (
            <div
              key={index + 1}
              style={{ background: 'url(' + text.link + ')' }}
              className="cslider-item"
            >
              <div className="cslider-info">
                <h3 className="cslider-title">{text.title}</h3>
                <h5 className="cslider-subtitle">{text.subtitle}</h5>
              </div>
            </div>
          ))}
      </div>
      <span className="cslider-arrow-right" onClick={pgRight}>
        <FontAwesomeIcon icon={faArrowRight} />
      </span>
    </div>
  );
};

export default CustomSlider;
