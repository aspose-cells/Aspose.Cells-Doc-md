---
title: Темы и цвета Excel
type: docs
weight: 100
url: /ru/net/excel-themes-and-colors/
---
## **Темы и цвета Excel**

Темы обеспечивают единый внешний вид с именованными стилями, графическими эффектами и другими объектами, используемыми в книге. Например, стиль Accent1 выглядит по-разному в темах Office и Apex. Часто вы применяете тему документа, а затем изменяете ее по своему усмотрению.

Aspose.Cells предоставляет функции для настройки тем и цветов.

### **Получить и установить цвета темы**

Ниже приведены несколько методов и свойств, реализующих цвета темы.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Используется для установки цвета переднего плана.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Используется для установки цвета фона.
- [**Шрифт.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Используется для установки цвета шрифта.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Используется для получения цвета темы.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Используется для установки цвета темы.

В следующем примере показано, как получить и установить цвета темы.

В следующем примере используется файл шаблона XLSX, получаются цвета для различных типов цветов темы, изменяются цвета и сохраняется файл Excel Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

#### **Настроить темы**

В следующем примере показано, как применить пользовательские темы с нужными цветами. Мы используем образец файла шаблона, созданный вручную в Microsoft Excel 2007.

В следующем примере загружается файл шаблона XLSX, определяются цвета для различных типов цветов темы, применяются пользовательские цвета и сохраняется файл Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

#### **Используйте цвета темы**

В следующем примере применяются цвета переднего плана и шрифта ячейки на основе типов цветов темы по умолчанию (рабочей книги). Он также сохраняет файл Excel на диск.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

## **Предварительные темы**
- [Извлечь данные темы из файла Excel](/cells/ru/net/extract-theme-data-from-excel-file/)
