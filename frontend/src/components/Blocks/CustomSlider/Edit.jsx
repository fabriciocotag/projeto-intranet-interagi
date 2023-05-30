import './Block.css';

import React, { useState } from 'react';

const CustomSlider = (props) => {
  const { data, onChangeBlock } = props;
  const [texts, setTexts] = useState(data.texts || []);

  const handleChange = (index, field, value) => {
    const updatedTexts = [...texts];
    updatedTexts[index][field] = value;
    setTexts(updatedTexts);
    onChangeBlock(props.block, { ...data, texts: updatedTexts });
  };

  const handleAddText = () => {
    const newText = { title: '', subtitle: '', link: '' };
    const updatedTexts = [...texts, newText];
    setTexts(updatedTexts);
    onChangeBlock(props.block, { ...data, texts: updatedTexts });
  };

  const handleRemoveText = (index) => {
    const updatedTexts = [...texts];
    updatedTexts.splice(index, 1);
    setTexts(updatedTexts);
    onChangeBlock(props.block, { ...data, texts: updatedTexts });
  };

  return (
    <div className="component-cslider cslider-edit">
      <h5 className="cslider-title">Slides</h5>
      {texts.map((text, index) => (
        <div key={index} className="cslider-form">
          <input
            type="text"
            value={text.title}
            onChange={(e) => handleChange(index, 'title', e.target.value)}
            placeholder="Título"
          />
          <input
            type="text"
            value={text.subtitle}
            onChange={(e) => handleChange(index, 'subtitle', e.target.value)}
            placeholder="Subtítulo"
          />
          <input
            type="text"
            value={text.link}
            onChange={(e) => handleChange(index, 'link', e.target.value)}
            placeholder="URL da imagem"
          />
          <button
            onClick={() => handleRemoveText(index)}
            className="cslider-delete"
          >
            ×
          </button>
        </div>
      ))}
      <button onClick={handleAddText} className="cslider-new">
        Novo
      </button>
    </div>
  );
};

export default CustomSlider;
