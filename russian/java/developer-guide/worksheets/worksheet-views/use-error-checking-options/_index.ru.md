---
title: Использование опций проверки ошибок
type: docs
weight: 60
url: /ru/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

В Microsoft Excel пользователи могут определять опции и правила проверки ошибок. При создании формул пользователи часто видят проверку ошибок, маленький треугольник в верхнем правом углу ячейки выделяет проблему в ячейке. Excel предоставляет информацию, которая помогает пользователям исправить распространенные проблемы.

{{% /alert %}} 
## **Типы ошибок**
Ошибки, которые означают, что формула не может вернуть результат - например, деление числа на ноль - требуют немедленного внимания, и в ячейке отображается значение ошибки. Нажатие на зеленый треугольник показывает восклицательный знак, щелчок по которому открывает список опций. 

Ошибка может быть исправлена с помощью опций или проигнорирована. Игнорирование ошибки означает, что она больше не появится при последующих проверках ошибок.

Aspose.Cells предоставляет функции опций проверки ошибок. Класс ErrorCheckOptions управляет различными типами проверок ошибок, например, числа, сохраненные как текст, ошибки при вычислении формул и ошибки валидации. Используйте перечисление ErrorCheckType для установки желаемой проверки ошибок.
## **Числа, сохраненные как текст**
Иногда числа могут быть отформатированы и сохранены в ячейках как текст. Это может вызвать проблемы с вычислениями или привести к непонятным порядкам сортировки. Числа, отформатированные как текст, выровнены влево, а не вправо, в ячейке. Если формула, которая должна выполнить математическую операцию с ячейками, не возвращает значение, следует проверить выравнивание в ячейках, на которые ссылается формула - некоторые или все эти ячейки могут быть числами, отформатированными как текст.

Вы можете использовать опции проверки ошибок, чтобы быстро преобразовать числа, сохраненные как текст, в реальные числа. В Microsoft Excel 2003:

1. На меню **Инструменты** щелкните **Параметры**.
1. Выберите вкладку Проверка ошибок.
   Опция **Число сохранено как текст** установлена по умолчанию. 
1. Отключить ее.
   См. нижеприведенное изображение о том, как зеленый треугольник отображается для данных в MS Excel.

![todo:image_alt_text](use-error-checking-options_1.png)

Приведенный ниже образец кода показывает, как отключить опцию проверки ошибок чисел, сохраненных как текст, для листа в файле-шаблоне XLS, используя API Aspose.Cells. 

**Java**

{{< highlight csharp >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
