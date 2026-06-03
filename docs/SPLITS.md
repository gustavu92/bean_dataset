# Dataset Splits

This dataset provides two predefined split protocols.

## Train/Validation/Test Split

The train/validation/test split was generated with a fixed random seed.

- Seed: 42
- Total images: 228
- Train: 160 images
- Validation: 34 images
- Test: 34 images
- Ratio: 70/15/15

Image lists:

```text
splits/train_val_test/train.txt
splits/train_val_test/val.txt
splits/train_val_test/test.txt
```

COCO annotation files:

```text
annotations/splits/train_val_test/train.json
annotations/splits/train_val_test/val.json
annotations/splits/train_val_test/test.json
```

## 5-Fold Cross-Validation Split

The 5-fold split was generated with a fixed random seed.

- Seed: 42
- Total images: 228

Fold sizes:

| Fold | Train | Test |
|-----:|------:|-----:|
| 1 | 182 | 46 |
| 2 | 182 | 46 |
| 3 | 182 | 46 |
| 4 | 183 | 45 |
| 5 | 183 | 45 |

Image lists:

```text
splits/5fold/fold_1/train.txt
splits/5fold/fold_1/test.txt
splits/5fold/fold_2/train.txt
splits/5fold/fold_2/test.txt
splits/5fold/fold_3/train.txt
splits/5fold/fold_3/test.txt
splits/5fold/fold_4/train.txt
splits/5fold/fold_4/test.txt
splits/5fold/fold_5/train.txt
splits/5fold/fold_5/test.txt
```

COCO annotation files:

```text
annotations/splits/5fold/fold_1/train.json
annotations/splits/5fold/fold_1/test.json
annotations/splits/5fold/fold_2/train.json
annotations/splits/5fold/fold_2/test.json
annotations/splits/5fold/fold_3/train.json
annotations/splits/5fold/fold_3/test.json
annotations/splits/5fold/fold_4/train.json
annotations/splits/5fold/fold_4/test.json
annotations/splits/5fold/fold_5/train.json
annotations/splits/5fold/fold_5/test.json
```

## Important Note

These splits were generated for convenience and reproducibility. They should not be interpreted as the exact original splits used in the paper unless explicitly stated.

The original paper reports a 5-fold evaluation protocol with 183 training images and 45 testing images per fold. The 5-fold split included in this release uses all 228 images exactly once as test data across folds. Because 228 is not divisible by 5, the test folds have 46, 46, 46, 45, and 45 images.
