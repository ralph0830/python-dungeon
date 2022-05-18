QPushButton button("Animated Button");
button.show();

QPropertyAnimation anim1(&button, "geometry");
anim1.setDuration(3000);
anim1.setStartValue(QRect(0, 0, 100, 30));
anim1.setEndValue(QRect(500, 500, 100, 30));

QPropertyAnimation anim2(&button, "geometry");
anim2.setDuration(3000);
anim2.setStartValue(QRect(500, 500, 100, 30));
anim2.setEndValue(QRect(1000, 500, 100, 30));

QSequentialAnimationGroup group;

group.addAnimation(&anim1);
group.addAnimation(&anim2);

group.start();