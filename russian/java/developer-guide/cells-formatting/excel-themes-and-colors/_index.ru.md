---
title: Темы и цвета Excel
type: docs
weight: 130
url: /ru/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

Темы обеспечивают единообразный внешний вид с именованными стилями, графическими эффектами и другими объектами, используемыми в книге. Например, стиль Accent1 выглядит по-другому в темах Office и Apex. Часто вы применяете тему документа, а затем настраиваете ее согласно вашим потребностям.

**Применение тем в Microsoft Excel**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Получение и установка цветов темы**

API Aspose.Cells предоставляет функции для настройки тем и цветов. Ниже перечислены несколько методов и свойств, реализующих цвета темы.

- Cвойство Style.ForegroundThemeColor можно использовать для установки цвета переднего плана.
- Cвойство Style.BackgroundThemeColor можно использовать для установки цвета фона.
- Cвойство Font.ThemeColor можно использовать для установки цвета шрифта.
- Метод Workbook.getThemeColor можно использовать для получения тематического цвета.
- Метод Workbook.setThemeColor можно использовать для установки тематического цвета.

В следующем примере показано, как получить и установить цвета темы.

В следующем примере используется шаблонный файл XLSX, получаются цвета для различных типов цветов темы, изменяются цвета и сохраняется файл Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Настройка тем**

Следующий пример показывает, как применять пользовательские темы с выбранными вами цветами. В примере используется образец шаблонного файла, созданного вручную в Microsoft Excel 2007.

**Файл шаблона CustomThemeColor.xlsx**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

Приведенный ниже пример загружает шаблонный файл XLSX, определяет цвета для различных типов цвета темы, применяет пользовательские цвета и сохраняет файл Excel.

**Сгенерированный файл с настроенными тематическими цветами**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Использование тематических цветов**

Приведенный ниже пример применяет передний план ячейки и цвета шрифта на основе цветов темы по умолчанию (рабочей книги). Он также сохраняет файл Excel на диск.

Следующий вывод генерируется при выполнении кода.

**Тематические цвета, примененные к ячейке D3 рабочего листа** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Продвинутые темы**
- [Извлечение данных о теме из файла Excel](/cells/ru/java/extract-theme-data-from-excel-file/)
