---
title: Aspose.Cells for Java  مكتبة قابلة للانقطاع
type: docs
weight: 1090
url: /ar/java/aspose-cells-for-java-interruptible-library/
---

{{% alert color="primary" %}}

تدعم Aspose.Cells for Java إعاقة عملية التحميل/الحفظ أثناء العمل مع ملفات Excel الكبيرة. في بعض الأحيان، ترغب في جعل المكتبات/المكونات قابلة للانقطاع. سيؤثر هذا بالتأكيد على كفاءة وموثوقية خدماتك/عملياتك. يمكنك التخلي بموثوقية عن جزء من التحويل عندما تكتشف أنه يستغرق وقتًا طويلاً. سيوفر ذلك استخدام وحدة المعالجة المركزية، الذاكرة العشوائية وما إلى ذلك. يعني ذلك أنك لا تحتاج إلى اتخاذ خطوات متطرفة مثل إيقاف خادم كامل فقط لإلغاء التحويل. 
{{% /alert %}}

## **مثال:**

يُظهر البرنامج التالي كيفية انقطاع عملية الحفظ باستخدام طريقة **InterruptMonitor.interrupt()**.

[**Java**]

{{< highlight java >}}

 //Create a new Workbook  

final Workbook wb = new Workbook();

// Get the Worksheets

WorksheetCollection wss = wb.getWorksheets();

// Run a loop to fill sheet cells with data

for (int i = 0; i < 50; i++) {

    Worksheet sheet = wss.get(wss.add());

    Cells cells = sheet.getCells();

    for (int row = 0; row < 5000; row++) {

        for (int col = 0; col < 10; col++) {

            cells.get(row, col).setValue(i * 5000 + row * 500 + col);

        }

    }

}

final InterruptMonitor monitor = new InterruptMonitor();

wb.setInterruptMonitor(monitor);

new Thread(new Runnable() {

    public void run() {

        try {

            Thread.sleep(Math.round(Math.random() * 3000));

        } catch (InterruptedException e) {

        }

        // Interrupt the process

        monitor.interrupt();

        System.out.println("Interrupting the save thread at "

                + System.currentTimeMillis());

    }

}).start();

try {

    wb.save("makeinterrupted.xlsx", FileFormatType.XLSX);

} catch (CellsException e) {

    if (e.getCode() == ExceptionType.INTERRUPTED) {

        System.out.println(e.getMessage());

        System.out.println("The save thread finishes at "

                + System.currentTimeMillis());

    } else {

        throw e;

    }

}

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
