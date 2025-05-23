---
title: Конвертировать диаграмму Excel в изображение
type: docs
weight: 20
url: /ru/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

Диаграммы наглядны и облегчают пользователю видеть сравнения, паттерны и тенденции в данных. Например, вместо анализа колонок чисел в таблице, диаграмма сразу показывает, уменьшаются ли продажи или растут, или сравнивает фактические продажи с плановыми. Людям часто приходится представлять статистическую и графическую информацию в легко понимаемой и легко поддерживаемой форме. Изображение помогает.

Иногда диаграммы нужны в приложении или на веб-страницах. Или может понадобиться для документа Word, файла PDF, презентации PowerPoint или другого приложения. В каждом случае нужно конвертировать диаграмму в изображение, чтобы можно было использовать ее в других местах.

{{% /alert %}}

## **Конвертация диаграмм в изображения**

В приведенных примерах круговая диаграмма и столбчатая диаграмма конвертируются в изображения.

### **Конвертация круговой диаграммы в файл изображения**

Сначала создайте круговую диаграмму в Microsoft Excel, а затем конвертируйте ее в файл изображения с помощью Aspose.Cells. Код в этом примере создает изображение EMF на основе круговой диаграммы в шаблонном файле Microsoft Excel.

|**Результат: изображение круговой диаграммы**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Создайте круговую диаграмму в Microsoft Excel:
   1. Откройте новую книгу в Microsoft Excel.
   1. Введите некоторые данные в лист.
   1. Создайте круговую диаграмму на основе данных.
   1. Сохраните файл.

|**Исходный файл.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Скачайте и установите Aspose.Cells:
   1. [Загрузить Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. Установите его на вашем компьютере для разработки.

Все компоненты [Aspose](http://www.aspose.com/) работают в режиме оценки при первой установке. Режим оценки не имеет временных ограничений и вставляет в выходные документы только водяной знак.

1. Создайте проект:
   1. Запустите Visual Studio.Net.
   1. Создайте новое консольное приложение. В этом примере используется консольное приложение на C#, но вы также можете использовать VB.NET.
   1. Добавьте ссылку. Этот проект использует Aspose.Cells, поэтому добавьте ссылку на Aspose.Cells, например ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
   1. Напишите код, который находит и конвертирует диаграмму. Приведен ниже код, используемый компонентом для выполнения задачи. Используется очень немного строк кода.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Конвертация столбчатой диаграммы в файл изображения**

Сначала создайте столбчатую диаграмму в Microsoft Excel и конвертируйте ее в файл изображения, как описано выше. После выполнения образца кода создается файл JPEG на основе столбчатой диаграммы в шаблонном файле Excel.

|**Выходной файл: изображение столбчатой диаграммы.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Создайте столбчатую диаграмму в Microsoft Excel:
   1. Откройте новую книгу в Microsoft Excel.
   1. Введите некоторые данные в лист.
   1. Создайте столбчатую диаграмму на основе данных.
   1. Сохраните файл.

|**Входной файл.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Создайте проект с ссылками, как описано выше.
1. Динамически преобразуйте диаграмму в изображение. Ниже приведен используемый компонентом код для выполнения этой задачи. Код аналогичен предыдущему:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
