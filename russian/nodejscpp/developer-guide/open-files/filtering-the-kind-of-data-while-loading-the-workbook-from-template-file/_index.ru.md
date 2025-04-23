---  
title: Фильтрация типа данных при загрузке книги из шаблонного файла с помощью Node.js через C++  
linktitle: Фильтрация типа данных при загрузке книги из файла шаблона  
type: docs  
weight: 400  
url: /ru/nodejs-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/  
---  

{{% alert color="primary" %}}  
Иногда вы хотите указать, какой тип данных должен быть загружен при создании книги из шаблона. Фильтрация загруженных данных может повысить производительность для ваших целей, особенно при использовании [LightCells API](/cells/ru/nodejs-cpp/using-lightcells-api/). Пожалуйста, используйте свойство [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) для этого.  
{{% /alert %}}  

Следующий пример кода загружает только объекты формы при загрузке книги из [шаблонного файла](5115552.xlsx), который вы можете скачать по ссылке. Следующий скриншот показывает содержимое [шаблонного файла](5115552.xlsx) и объясняет, что данные красного цвета и с желтым фоном не будут загружены, потому что свойство [**LoadOptions.getLoadFilter()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) установлено в [**Shape**](https://reference.aspose.com/cells/nodejs-cpp/shape/)  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)  

На следующем снимке экрана показан [выходной PDF](5115555.pdf), который вы можете скачать по указанной ссылке. Здесь вы можете видеть, что данные красного цвета и с желтым фоном отсутствуют, но все формы присутствуют.  

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Set the load options, we only want to load shapes and do not want to load data
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);            

loadOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Create workbook object from sample excel file using load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleFilterChars.xlsx"), loadOptions);

// Save the output in pdf format
workbook.save(outputDir + "sampleFilterChars_out.pdf", AsposeCells.SaveFormat.Pdf);
```  

