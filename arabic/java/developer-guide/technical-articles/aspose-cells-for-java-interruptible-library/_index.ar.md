---
title: Aspose.Cells for Java - المكتبة المتقطعة
type: docs
weight: 1090
url: /ar/java/aspose-cells-for-java-interruptible-library/
---
{{% alert color="primary" %}}

 Aspose.Cells for Java يدعم مقاطعة عملية التحميل / الحفظ أثناء العمل مع ملفات Excel الكبيرة. في بعض الأحيان ، تريد جعل المكتبات / المكونات قابلة للمقاطعة. سيؤدي هذا بالتأكيد إلى تحسين كفاءة وموثوقية خدماتك / عملياتك. يمكنك أن تتخلى عن التحويل بشكل موثوق عندما تكتشف أنه يستغرق وقتًا طويلاً. هذا من شأنه أن يوفر استخدام وحدة المعالجة المركزية ، وذاكرة الوصول العشوائي وما إلى ذلك. وهذا يعني أنك لست مضطرًا إلى اتخاذ خطوات جذرية مثل قتل الخادم بأكمله فقط لإلغاء التحويل.
{{% /alert %}}

## **مثال:**

 يوضح البرنامج التالي كيفية مقاطعة عملية الحفظ باستخدام**InterruptMonitor.interrupt ()** طريقة.

[**Java**]{{< highlight "java" >}}

 // إنشاء مصنف جديد

المصنف النهائي wb = مصنف جديد () ؛

// احصل على أوراق العمل

WorksheetCollection wss = wb.getWorksheets () ،

// قم بتشغيل حلقة لملء خلايا الورقة بالبيانات

 لـ (int i = 0 ؛ i< 50; i++) {

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
