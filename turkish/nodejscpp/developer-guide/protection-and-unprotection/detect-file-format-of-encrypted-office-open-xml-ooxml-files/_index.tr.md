---  
title: Şifreli Office Open XML  OOXML Dosyalarının Dosya Formatını Tanımlama ile Node.js kullanımı  
linktitle: Şifrelenmiş Office Open XML  OOXML Dosyasının Dosya Biçimini Algılama  
type: docs  
weight: 340  
url: /tr/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/  
description: Aspose.Cells for Node.js via C++ ile şifreli OOXML dosyalarının dosya formatını nasıl tespit edeceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  

**Office Open XML** (aynı zamanda **OOXML** veya **Microsoft Open XML** (MOX) olarak da bilinir), Microsoft tarafından geliştirilmiş ve ofis belgelerini (çeşitli elektronik tablo, grafik, sunum ve word işleme belgeleri) temsil eden XML tabanlı bir dosya formatıdır.  

{{% /alert %}}  

Aspose.Cells, şifreli **Microsoft Open XML** dosyalarının dosya formatını tespit etmenin bir yolunu sunar. Dosya türünü belirlemek için aşağıdaki örnekte gösterildiği gibi [FileFormatUtil.detectFileFormat(Uint8Array)] metodunu kullanabilirsiniz.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "encryptedBook1.out.tmp");

fs.writeFileSync(filePath, Buffer.from([0x50, 0x4B, 0x03, 0x04]));
const stream = fs.readFileSync(filePath);
AsposeCells.FileFormatUtil.verifyPassword(stream, "1234");
const fileFormatInfo = AsposeCells.FileFormatUtil.detectFileFormat(stream);

console.log("File Format: " + fileFormatInfo.getFileFormatType());
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
