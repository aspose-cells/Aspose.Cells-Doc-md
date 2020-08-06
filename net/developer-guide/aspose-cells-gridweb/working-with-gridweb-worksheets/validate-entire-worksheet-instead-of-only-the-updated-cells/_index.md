---
title: Validate entire worksheet instead of only the updated cells
type: docs
weight: 140
url: /net/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **Possible Usage Scenarios**
By default, GridWeb validates only the updated cells and does not validate the entire worksheet. However, if you want to validate entire worksheet on client side before GridWeb posts request to server, then you should set the needValidateall variable inside the acwmain.js to true.
## **Validate entire worksheet instead of only the updated cells**
The following screenshot displays the needValidateall variable in acwmain.js. Please set it to true and now GridWeb will validate your entire worksheet not just the updated cells.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)
