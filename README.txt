# Bean Dataset

Bean Dataset is an agricultural image dataset for semantic and instance segmentation of soil, crop, and weed regions in common bean fields.

The dataset was introduced in the paper:

**Low-Cost Robot for Agricultural Image Data Acquisition**  
Agriculture 2023, 13(2), 413  
https://doi.org/10.3390/agriculture13020413

Paper link:  
https://www.mdpi.com/2077-0472/13/2/413

## Preview

Main preview image: docs/preview_overlay.jpg

Additional paper figures are available in docs/.

Preview

Main README preview files:
- docs/preview_original.jpg
- docs/preview_overlay.jpg
- docs/bean_dataset_all_images.gif

Preview source image: 2021_05_06_20_12_14_823673.jpg
Description

This dataset contains RGB field images acquired in common bean crop areas using DARob, a low-cost agricultural robot developed for image data acquisition. The dataset supports the evaluation of computer vision methods for crop, weed, and soil segmentation in agricultural environments.

The crop used in the dataset is common bean, *Phaseolus vulgaris L.* Data were collected in an experimental area at the School of Agricultural Engineering (FEAGRI), University of Campinas (UNICAMP), Brazil.

The image acquisition process covered different growth stages of the bean crop under different field and lighting conditions. The annotated subset focuses on plants approximately 2 to 3 weeks into the growth stage, matching stages commonly used in other agricultural segmentation datasets.

## Dataset Summary

| Item | Value |
|------|------:|
| Annotated RGB images | 228 |
| Image resolution | 704 x 480 pixels |
| Annotation format | COCO segmentation |
| Annotation instances | 697 |
| Classes | 3 |

## Classes

| ID | Class |
|---:|-------|
| 1 | Soil |
| 2 | Crop |
| 3 | Weed |

## Class Distribution

According to the original paper, the annotated dataset contains the following pixel-area distribution:

| Class | Area |
|------|------:|
| Soil | 75.10% |
| Crop | 17.30% |
| Weed | 7.58% |

## Dataset Structure

```text
bean_dataset_coco_v1.0.0/
├── README.md
├── README.txt
├── LICENSE
├── CITATION.bib
├── annotations/
│   ├── instances.json
│   └── splits/
├── images/
├── splits/
├── metadata/
├── scripts/
└── docs/
```

The main annotation file is:

```text
annotations/instances.json
```

This file follows the COCO annotation format and contains the image metadata, categories, and segmentation annotations.

## Available Splits

This release includes two predefined split protocols:

1. Train/validation/test split
2. 5-fold cross-validation split

Both split protocols are available as plain text file lists and as independent COCO annotation files.

See `docs/SPLITS.md` for details.

## Benchmark Protocol from the Paper

In the original paper, the dataset was evaluated using five k-fold splits. Each fold contains:

- 183 training images
- 45 testing images

The benchmark models reported in the paper include:

- BiSeNet with ResNet-18 backbone
- DuNet with ResNet-50 backbone
- DeepLab-v3 with ResNet-50 backbone
- DeepLab-v3+ with ResNet-50 backbone
- PSPNet with ResNet-50 backbone

The reported mean IoU values in the paper are:

| Model | Soil | Crop | Weed | Mean |
|-------|-----:|-----:|-----:|-----:|
| BiSeNet (ResNet-18) | 0.942 | 0.920 | 0.625 | 0.829 |
| DuNet (ResNet-50) | 0.950 | 0.927 | 0.662 | 0.846 |
| DeepLab-v3 (ResNet-50) | 0.953 | 0.935 | 0.680 | 0.856 |
| DeepLab-v3+ (ResNet-50) | 0.957 | 0.958 | 0.682 | 0.866 |
| PSPNet (ResNet-50) | 0.959 | 0.940 | 0.708 | 0.869 |

## Usage

Validate the dataset:

```bash
python scripts/verify_coco.py
```

Validate the predefined splits:

```bash
python scripts/verify_splits.py
```

Load the COCO annotations with the example script:

```bash
python scripts/example_load_coco.py
```

## Citation

If you use this dataset in your research, please cite the original paper:

```bibtex
@article{vasconcelos2023lowcost,
  title = {Low-Cost Robot for Agricultural Image Data Acquisition},
  author = {Vasconcelos, Gustavo Jos{\'e} Querino and Costa, Gabriel Schubert Ruiz and Spina, Thiago Vallin and Pedrini, Helio},
  journal = {Agriculture},
  volume = {13},
  number = {2},
  article-number = {413},
  year = {2023},
  doi = {10.3390/agriculture13020413},
  url = {https://www.mdpi.com/2077-0472/13/2/413}
}
```

## License

This dataset is licensed under the Creative Commons Attribution 4.0 International License.

See `LICENSE` for details.
