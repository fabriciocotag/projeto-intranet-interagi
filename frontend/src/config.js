/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */
// All your imports required for the config here BEFORE this line
import '@plone/volto/config';
import SliderIcon from '@plone/volto/icons/megaphone.svg';

import CustomSlider from './components/Blocks/CustomSlider/View';
import CustomSliderEdit from './components/Blocks/CustomSlider/Edit';

export default function applyConfig(config) {
  config.blocks.blocksConfig.customslider = {
    id: 'customslider',
    title: 'Slides Personalizados',
    group: 'text',
    icon: SliderIcon,
    view: CustomSlider,
    edit: CustomSliderEdit,
    restricted: false,
    mostUsed: false,
    sidebarTab: false,
    blockHasOwnFocusManagement: false,
  };

  return config;
}
