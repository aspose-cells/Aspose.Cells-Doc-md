---
title: C++でワークブックのアンマネージドリソースを解放する
linktitle: ブックのアンマネージリソースを解放する
type: docs
weight: 310
url: /ja/cpp/release-unmanaged-resources-of-the-workbook/
description: Aspose.Cellsを使用してC++でワークブックのアンマネージドリソースを解放する方法を学びましょう。
---

{{% alert color="primary" %}}

Aspose.Cellsは、[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) オブジェクトのアンマネージリソースを解放するための [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) メソッドを提供しています。Disposeパターンは、ファイルやパイプハンドル、レジストリハンドル、待機ハンドル、またはアンマネージメモリブロックへのポインタなど、アンマネージリソースにアクセスするオブジェクトにだけ使用されます。これは、ガベージコレクタが未使用の管理オブジェクトを効率的に回収することができる一方で、アンマネージオブジェクトを回収することができないためです。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)オブジェクトは、単一のメソッド[**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/)を持つ*IDisposable*インターフェースを実装しています。[**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/)メソッドを直接呼び出すか、*Using*ステートメントを使用して自動的にこのメソッドを呼び出すことができます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
