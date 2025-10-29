---
title: استخدام واجهة برمجة تطبيقات LightCells مع C++
linktitle: استخدام واجهة LightCells API
type: docs
weight: 160
url: /ar/cpp/using-lightcells-api/
description: تعلم كيفية استخدام واجهة برمجة تطبيقات LightCells في C++ لقراءة وكتابة ملفات إكسل كبيرة بكفاءة مع أقل استخدام للذاكرة.
---

{{% alert color="primary" %}} 

في بعض الأحيان تحتاج إلى قراءة وكتابة ملفات Microsoft Excel الكبيرة بقائمة كبيرة من البيانات أو المحتوى في ورقة العمل. واجهة برمجة التطبيقات المبسطة مفيدة لإنشاء جداول بيانات Excel الضخمة: معها، تحتاج إلى أقل كمية من الذاكرة وتحصل على أداء وكفاءة أفضل.

{{% /alert %}} 

# الهندسة المعمارية المدفوعة بالأحداث
توفر Aspose.Cells واجهة LightCells API مصممة بشكل رئيسي للتلاعب ببيانات الخلية واحدة تلو الأخرى دون بناء نموذج بيانات كاملاً (باستخدام مجموعة الخلية إلخ) في الذاكرة. تعمل في وضع محفز بالأحداث.

لحفظ دفاتر العمل، يتم تقديم محتوى الخلية خلية بخلية عند الحفظ، ويقوم المكون بحفظه في ملف الإخراج مباشرةً.

عند قراءة ملفات القالب، يُحلل المكون كل خلية ويقدم قيمها واحدة تلو الأخرى.

في كل من الإجراءين، يتم معالجة كائن Cell ومن ثم التخلّص منه، ولا يحمل كائن Workbook المجموعة. وبالتالي، يتم توفير الذاكرة عند استيراد وتصدير ملف Microsoft Excel الذي يحتوي على مجموعة بيانات كبيرة والتي ستستخدم وحدة كبيرة من الذاكرة وإلا.

على الرغم من أن واجهة LightCells API تعالج الخلايا بنفس الطريقة لملفات XLSX وXLS (حيث لا تقوم فعليًا بتحميل كل الخلايا في الذاكرة ولكن تعالج خلية ومن ثم تتخلص منها)، إلا أنها تحفظ الذاكرة بشكل أكثر فعالية لملفات XLSX من ملفات XLS بسبب النماذج والهياكل المختلفة للصيغتين.

ومع ذلك، **بالنسبة لملفات XLS**، يمكن للمطورين تحديد موقع مؤقت لحفظ البيانات المؤقتة التي تُولد أثناء عملية الحفظ، لتحفيظ المزيد من الذاكرة. بشكل شائع، **يمكن لاستخدام واجهة LightCells API لحفظ ملف XLSX توفير 50% أو أكثر من الذاكرة** مقارنة بالطريقة الشائعة، **حفظ ملف XLS قد يوفر حوالي 20-40% من الذاكرة**.

## كتابة ملف إكسل كبير
 توفر Aspose.Cells واجهة، `LightCellsDataProvider`، يجب تنفيذها في برنامجك. تمثل الواجهة مزود البيانات لحفظ ملفات جداول البيانات الكبيرة في وضع خفيف الوزن.

عند حفظ ملف عمل باستخدام هذا الوضع، يتم التحقق من `StartSheet(int)` عند حفظ كل ورقة عمل في الملف. لورقة واحدة، إذا كانت `StartSheet(int)` تساوي صحيح، فإن جميع بيانات وخصائص الصفوف والخلايا في هذه الورقة التي سيتم حفظها يتم توفيرها بواسطة هذا التطبيق. في المقام الأول، يتم استدعاء `NextRow()` للحصول على فهرس الصف التالي للحفظ. إذا تم إرجاع فهرس صف صالح (يجب أن يكون فهرس الصف بترتيب تصاعدي للصفوف التي سيتم حفظها)، يتم توفير كائن `Row` يمثل هذا الصف ليتم ضبط خصائصه بواسطة `StartRow(Row)`.

بالنسبة لصف واحد، يتم التحقق أولاً من `NextCell()`. إذا تم إرجاع فهرس عمود صالح (يجب أن يكون فهرس العمود بترتيب تصاعدي لجميع الخلايا في صف واحد للحفظ)، يتم توفير كائن `Cell` يمثل تلك الخلية ليتم ضبط بياناتها وخصائصها بواسطة `StartCell(Cell)`. بعد ضبط بيانات الخلية، يتم حفظها مباشرة في ملف الجدول الناتج ويتم التحقق من الخلية التالية ومعالجتها.

### كتابة ملف إكسل كبير: مثال
يرجى رؤية الكود النموذجي التالي لرؤية عمل واجهة برمجة التطبيقات (API) LightCells. أضف وأزل، أو حدث الشرائح التوضيحية وفقًا لاحتياجاتك.

 ينشئ البرنامج ملفًا ضخمًا يحتوي على **10,000 (مصفوفة 10000×30)** سجل في ورقة عمل ويملاها ببيانات وهمية. يمكنك تحديد مصفوفة خاصة بك بتغيير متغيري `rowsCount` و `colsCount` في طريقة `Main()`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestDataProvider : public LightCellsDataProvider {
private:
    int _row = -1;
    int _column = -1;
    int maxRows;
    int maxColumns;
    Workbook _workbook;

public:
    TestDataProvider(Workbook workbook, int maxRows, int maxColumns)
        : _workbook(workbook), maxRows(maxRows), maxColumns(maxColumns) {}

    bool IsGatherString() override {
        return false;
    }

    int NextCell() override {
        ++_column;
        if (_column < this->maxColumns)
            return _column;
        else {
            _column = -1;
            return -1;
        }
    }

    int NextRow() override {
        ++_row;
        if (_row < this->maxRows) {
            _column = -1;
            return _row;
        }
        else
            return -1;
    }

    void StartCell(Cell& cell) override {
        cell.PutValue(_row + _column);
        if (_row != 1) {
            cell.SetFormula(u"=Rand() + A2");
        }
    }

    void StartRow(Row& row) override {}

    bool StartSheet(int sheetIndex) override {
        return sheetIndex == 0;
    }
};

void WriteUsingLightCellsAPI() {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    int rowsCount = 10000;
    int colsCount = 30;

    Workbook workbook;
    OoxmlSaveOptions ooxmlSaveOptions;

    TestDataProvider dataProvider(workbook, rowsCount, colsCount);
    ooxmlSaveOptions.SetLightCellsDataProvider(&dataProvider);

    workbook.Save(outDir + u"output.out.xlsx", ooxmlSaveOptions);

    std::cout << "File saved successfully using LightCells API!" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    WriteUsingLightCellsAPI();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## قراءة ملفات إكسل الكبيرة
توفر Aspose.Cells واجهة برمجة تطبيقات، `LightCellsDataHandler`، والتي يجب تنفيذها في برنامجك. تمثل الواجهة مزود البيانات لقراءة ملفات الجدول الكبيرة في وضع خفيف الوزن.

عند قراءة ملف عمل في هذا الوضع، يتم التحقق من `StartSheet` عند قراءة كل ورقة عمل في الملف. إذا كانت `StartSheet` ترجع صحيح، يتم فحص ومعالجة جميع بيانات وخصائص الخلايا في الصفوف والأعمدة في الورقة من قبل تنفيذ هذه الواجهة. يتم استدعاء `StartRow` لكل صف للتحقق مما إذا كان يجب معالجته. إذا كان الصف يحتاج إلى المعالجة، تتم قراءة خصائصه أولاً ويمكن للمطور الوصول إلى خصائصه بـ `ProcessRow`. إذا كانت خلايا الصف أيضًا بحاجة إلى المعالجة، يجب أن يعيد `ProcessRow` القيمة true ثم يتم استدعاء `StartCell` لكل خلية موجودة في الصف للتحقق مما إذا كانت بحاجة إلى المعالجة. إذا كانت خلية واحدة بحاجة إلى المعالجة، يتم استدعاء `ProcessCell` لمعالجة الخلية بواسطة تنفيذ هذه الواجهة.

### قراءة ملفات إكسل كبيرة: مثال
يرجى رؤية الكود النموذجي التالي لرؤية عمل واجهة برمجة التطبيقات (API) LightCells. أضف وأزل، أو حدث الشرائح التوضيحية وفقًا لاحتياجاتك.

البرنامج يقرأ ملفاً ضخمًا يحتوي على ملايين السجلات في ورقة عمل. يستغرق الأمر بعض الوقت لقراءة كل ورقة في دفتر العمل. يقرأ الكود النموذجي الملف ويسترجع العدد الإجمالي للخلايا، وعدد السلاسل وعدد الصيغ في كل ورقة عمل.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class LightCellsDataHandlerVisitCells : public LightCellsDataHandler
{
private:
    int cellCount;
    int formulaCount;
    int stringCount;

public:
    LightCellsDataHandlerVisitCells() : cellCount(0), formulaCount(0), stringCount(0) {}

    int GetCellCount() const { return cellCount; }
    int GetFormulaCount() const { return formulaCount; }
    int GetStringCount() const { return stringCount; }

    bool StartSheet(Worksheet& sheet) override
    {
        std::cout << "Processing sheet[" << sheet.GetName().ToUtf8() << "]" << std::endl;
        return true;
    }

    bool StartRow(int32_t rowIndex) override
    {
        return true;
    }

    bool ProcessRow(Row& row) override
    {
        return true;
    }

    bool StartCell(int32_t columnIndex) override
    {
        return true;
    }

    bool ProcessCell(Cell& cell) override
    {
        cellCount++;
        if (cell.IsFormula())
        {
            formulaCount++;
        }
        else if (cell.GetType() == CellValueType::IsString)
        {
            stringCount++;
        }
        return false;
    }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options and set the light cells data handler
    LoadOptions opts;
    auto handler = std::make_shared<LightCellsDataHandlerVisitCells>();
    opts.SetLightCellsDataHandler(handler.get());

    // Load the workbook with the specified options
    Workbook wb(srcDir + u"LargeBook1.xlsx", opts);

    // Get the total number of sheets
    int sheetCount = wb.GetWorksheets().GetCount();

    // Output the results
    std::cout << "Total sheets: " << sheetCount << ", cells: " << handler->GetCellCount()
              << ", strings: " << handler->GetStringCount() << ", formulas: " << handler->GetFormulaCount() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
