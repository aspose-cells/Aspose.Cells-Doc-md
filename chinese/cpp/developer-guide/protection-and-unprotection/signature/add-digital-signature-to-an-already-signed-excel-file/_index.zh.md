---
title: 使用C++向已签名的Excel文件添加数字签名
linktitle: 向已签名的Excel文件添加数字签名
type: docs
weight: 20
url: /zh/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: 学习如何使用Aspose.Cells for C++向已签名的Excel文件添加数字签名。通过多重签名保持文档完整性。
keywords: 向已签名的Excel文件添加数字签名，C++数字签名，Excel文档安全
---

## **可能的使用场景**

 Aspose.Cells提供[**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/)方法向已签名的Excel文件添加数字签名。

{{% alert color="primary" %}}

 添加数字签名到已签名的Excel文档时的注意事项：如果原始文档由Aspose.Cells生成，则功能正常。但如果文档由其他引擎（如Microsoft Excel）创建，Aspose.Cells for C++无法在加载和重新保存后保持精确的文件结构，可能会使现有签名失效。

{{% /alert %}}

## **如何向已经签名的Excel文件添加数字签名**

 以下示例代码演示了如何使用 [**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/) 在已签名的Excel文件中添加数字签名。示例Excel文件（50528280.xlsx）已预先签名。输出文件（50528281.xlsx）展示了效果。我们使用带密码的演示证书 [AsposeDemo.pfx](50528279.pfx)，密码为 **aspose**。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Certificate and workbook paths
    U16String certFilePath = srcDir + u"AsposeDemo.pfx";
    U16String inputFilePath = srcDir + u"sampleDigitallySignedByCells.xlsx";
    U16String outputFilePath = outDir + u"outputDigitallySignedByCells.xlsx";

    // Load digitally signed workbook
    Workbook workbook(inputFilePath);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;

    // Create digital signature using PFX certificate
    U16String password = u"aspose";
    U16String comments = u"Aspose.Cells added new digital signature in existing digitally signed workbook.";
    DigitalSignature signature(certFilePath, password, comments, Date());

    // Add signature to collection
    dsCollection.Add(signature);

    // Apply digital signatures to workbook
    workbook.AddDigitalSignature(dsCollection);

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "Digital signature added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
