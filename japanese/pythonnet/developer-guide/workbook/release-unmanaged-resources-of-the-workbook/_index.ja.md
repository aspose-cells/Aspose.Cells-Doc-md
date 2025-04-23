---
title: Python via .NETでワークブックの未管理リソースを解放する
linktitle: 未管理リソースを解放する
type: docs
weight: 310
url: /ja/python-net/release-unmanaged-resources-of-the-workbook/
description: Aspose.Cells for Python via .NETを使用してExcelワークブックで作業するときに未管理リソースを適切に解放する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは、[**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)メソッドを提供し、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)オブジェクトの未管理リソースを解放します。このパターンは、ファイルハンドル、ストリーム、またはメモリアロケーションなどの未管理リソースを扱う上で重要です。これらはPythonのガベージコレクターによって自動的に管理されません。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスは、Pythonのコンテキストマネージャプロトコルをリソース管理のために実装しています。明示的に[**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)メソッドを呼び出すか、Pythonの`with`ステートメントを使用して適切にクリーンアップすることができます。

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
