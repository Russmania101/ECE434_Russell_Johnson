cmd_/home/debian/exploringBB/extras/kernel/hello/hello.ko := ld -EL -r  -T ./scripts/module-common.lds --build-id  -T ./arch/arm/kernel/module.lds -o /home/debian/exploringBB/extras/kernel/hello/hello.ko /home/debian/exploringBB/extras/kernel/hello/hello.o /home/debian/exploringBB/extras/kernel/hello/hello.mod.o ;  true