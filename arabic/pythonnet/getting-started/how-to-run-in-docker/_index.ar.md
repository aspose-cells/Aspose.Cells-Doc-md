---
title: كيفية تشغيل Aspose.Cells لبايثون via .NET في Docker
type: docs
description: "تشغيل Aspose.Cells في حاوية Docker لنظام لينوكس"
weight: 140
url: /ar/net/how-to-run-aspose-cells-python-via-net-in-docker/
---

## مقدمـــــة:

يستخدم المزيد والمزيد من المستخدمين منتجات شركتنا المختلفة في دوكر، ويواجهون مشاكل مختلفة. تقدم هذه المقالة مقدمة مختصرة لكيفية استخدام Aspose.Cells لبايثون via .NET في بيئة دوكر بناءً على لينكس ديبيان.

## مثال:

نوضح الاستخدام بمثال بسيط. في هذه الحالة، الوظيفة بسيطة جدًا، فقط فتح ملف إكسل يحتوي على نص ياباني في aspose_test.py. هنا، نستخدم python:3.11 كصورة أساسية، وملف Dockerfile هو كما يلي:

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

ثم، عندما نقوم بتشغيل الأمر التالي، نحصل على النتيجة النهائية:
- بناء صورة Docker

{{< highlight plain >}}
docker build -t python_test .
{{< /highlight >}}

- تشغيل صورة Docker

{{< highlight plain >}}
docker run python_test 
{{< /highlight >}}

## ملاحظة:

لدعم فتح ملفات إكسل التي تحتوي على لغات متنوعة، نحتاج إلى تثبيت ICU. مع الأخذ في الاعتبار أن غطاء بايثون via .NET يعتمد على .NET Core 3.1، وأن .NET Core 3.1 لديه متطلبات إصدار محددة لـ ICU، والتي لا ينبغي أن تتجاوز الإصدار 70، فنحن بحاجة إلى تثبيت إصدار معين من ICU.


## انظر أيضاً

- [تثبيت Docker Desktop على Windows](https://docs.docker.com/docker-for-windows/install/)
{{< app/cells/assistant language="python-net" >}}
