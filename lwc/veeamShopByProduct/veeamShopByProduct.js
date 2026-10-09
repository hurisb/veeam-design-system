import { LightningElement, api } from 'lwc';

/**
 * Default four Veeam product lines. Each item:
 *   id          unique key (string)
 *   count       small badge, top-left (e.g. "4 editions")
 *   title       card heading
 *   description supporting copy
 *   cta         link label at the bottom
 *   url         link target
 *   icon        one of: shield-tick | grid-01 | download-cloud-02 | safe
 */
const DEFAULT_CATEGORIES = [
    {
        id: 'data-platform',
        count: '4 editions',
        title: 'Veeam Data Platform',
        description:
            'Compare Essentials, Foundation, Advanced and Premium for VMware, Hyper-V, Nutanix and physical servers.',
        cta: 'Compare editions',
        url: '#',
        icon: 'shield-tick'
    },
    {
        id: 'm365-backup',
        count: '3 plans',
        title: 'Microsoft 365 backup',
        description:
            'Protect Exchange Online, SharePoint, OneDrive and Teams — self-managed or as a service.',
        cta: 'Browse plans',
        url: '#',
        icon: 'grid-01'
    },
    {
        id: 'data-cloud',
        count: '6 workloads',
        title: 'Veeam Data Cloud',
        description:
            'Fully managed SaaS backup for Salesforce, Microsoft Entra ID, Azure and more — no infrastructure to run.',
        cta: 'Explore solutions',
        url: '#',
        icon: 'download-cloud-02'
    },
    {
        id: 'secure-storage',
        count: 'Per TB',
        title: 'Secure cloud storage',
        description:
            'Veeam Vault: fully managed, immutable object storage — air-gapped and ready for offsite backup.',
        cta: 'Shop Veeam Vault',
        url: '#',
        icon: 'safe'
    }
];

export default class VeeamShopByProduct extends LightningElement {
    // Section header — editable in Experience Builder (or set as attributes).
    @api eyebrow = 'Start here';
    @api heading = 'Shop by product';
    @api intro =
        'Go straight to pricing and editions for the products you already know or use.';
    @api viewAllLabel = 'Shop all Veeam products';
    @api viewAllUrl = '#';

    /**
     * Optional JSON array to override the four defaults (handy for Experience
     * Builder or a CMS). Must be an array of the shape documented above.
     * Invalid JSON falls back to the defaults.
     */
    @api categoriesJson;

    get categories() {
        if (this.categoriesJson) {
            try {
                const parsed = JSON.parse(this.categoriesJson);
                if (Array.isArray(parsed) && parsed.length) {
                    return parsed;
                }
            } catch (error) {
                // eslint-disable-next-line no-console
                console.warn(
                    'veeamShopByProduct: categoriesJson is not valid JSON — using defaults.',
                    error
                );
            }
        }
        return DEFAULT_CATEGORIES;
    }
}
