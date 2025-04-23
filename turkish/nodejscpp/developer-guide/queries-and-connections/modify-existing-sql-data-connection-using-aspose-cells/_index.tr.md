---  
title: Mevcut SQL Veri Bağlantısını Aspose.Cells for Node.js via C++ kullanarak değiştirin  
linktitle: Mevcut SQL Veri Bağlantısını Değiştirme Aspose.Cells ile  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Aspose.Cells for Node.js via C++ kullanarak mevcut SQL Veri Bağlantısı özelliklerini nasıl değiştireceğinizi öğrenin.  
---  

{{% alert color="primary" %}}  
Aspose.Cells, mevcut SQL Veri Bağlantısını değiştirme işlemini destekler. Bu makale, Aspose.Cells'ı kullanarak SQL Veri Bağlantısının farklı özelliklerini değiştirmeyi açıklamaktadır.  
Microsoft Excel içinde Veri > Bağlantılar menü komutunu kullanarak Veri Bağlantılarını ekleyebilir veya görüntüleyebilirsiniz.  
Benzer şekilde, Aspose.Cells çalışma kitabı.dataConnections koleksiyonunu kullanarak Veri Bağlantılarına erişim ve değiştirme sağlar.  
{{% /alert %}}  

## Aspose.Cells ile Mevcut SQL Veri Bağlantısını Değiştirme  

Aşağıdaki örnek, çalışma kitabının SQL Veri Bağlantısını değiştirmek için Aspose.Cells for Node.js via C++ kullanımını gösterir. Bu kodda kullanılan kaynak Excel dosyasını ve kod tarafından üretilen çıktı Excel dosyasını aşağıdaki bağlantılardan indirebilirsiniz.  

- [Kaynak Excel Dosyası](5112357.xlsx)  
- [Çıktı Excel Dosyası](5112356.xlsx)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataConnection.xlsx"));


// Access first Data Connection
const conn = workbook.getDataConnections().get(0);

// Change the Data Connection Name and Odc file
conn.setName("MyConnectionName");
conn.setOdcFile("C:\\Users\\MyDefaulConnection.odc");

// Change the Command Type, Command and Connection String
const dbConn = conn;
dbConn.setCommandType(AsposeCells.OLEDBCommandType.SqlStatement);
dbConn.setCommand("Select * from AdminTable");
dbConn.setConnectionString("Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

