import { LightningElement, api } from 'lwc';

/**
 * Renders a single Untitled UI line icon (24px grid, 2px stroke, currentColor)
 * selected by name. Size comes from the parent (set width/height on the
 * <c-veeam-product-icon> element); colour is inherited via `currentColor`.
 *
 * Supported names: 'shield-tick' | 'grid-01' | 'download-cloud-02' | 'safe'.
 */
export default class VeeamProductIcon extends LightningElement {
    @api iconName;

    get isShieldTick() {
        return this.iconName === 'shield-tick';
    }
    get isGrid() {
        return this.iconName === 'grid-01';
    }
    get isDownloadCloud() {
        return this.iconName === 'download-cloud-02';
    }
    get isSafe() {
        return this.iconName === 'safe';
    }
}
