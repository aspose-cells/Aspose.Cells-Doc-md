---
title: كيفية تشغيل Aspose.Cells لـ python via .NET في دوكر
type: docs
description: "تشغيل Aspose.Cells في حاوية Docker لنظام التشغيل Linux"
weight: 140
url: /ar/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## مقدمة:

يستخدم مزيد ومزيد من المستخدمين منتجات شركتنا المختلفة في الدوكر، ويواجهون مشاكل مختلفة. يقدم هذا المقال نبذة موجزة عن كيفية استخدام Aspose.Cells لـ Python via .NET في بيئة دوكر مستندة إلى Debian Linux.

## مثال:

نوضح الاستخدام من خلال مثال بسيط. في هذه الحالة، تكون الوظيفة بسيطة جدًا، فقط فتح ملف Excel يحتوي على نص ياباني في aspose_test.py. هنا، نستخدم python:3.11 كصورة أساسية، والملف النصي للدوكر المقابل كما يلي:

{{< highlight plain >}}
FROM python:3.11 AS base

# For drawing,e.g. convert to PDF
RUN apt-get update && apt-get install -y libgdiplus

# Install ICU version supported by .NET Core 3.1
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/i/icu/libicu70_70.1-2_amd64.deb
RUN dpkg -i libicu70_70.1-2_amd64.deb

RUN pip install -i aspose-cells-python
CMD ["python", "aspose_test.py"]
{{< /highlight >}}

ثم ، عند تشغيل الأمر التالي ، نحصل على النتيجة النهائية:
- بناء صورة Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- تشغيل صورة Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

-ملاحظة:

لدعم فتح ملفات Excel الذي تحتوي على لغات مختلفة ، نحتاج إلى تثبيت ICU. نظرًا لأن المحمل الخاص بلغة Python via .NET مبني على .NET Core 3.1 ، و. NET Core 3.1 لديه متطلبات خاصة لإصدار ICU ، الذي يجب ألا يتجاوز الإصدار 70 ، نحتاج إلى تثبيت إصدار محدد من ICU.


## انظر أيضاً

- [تثبيت Docker Desktop على Windows](https://docs.docker.com/docker-for-windows/install/)
