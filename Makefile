CC=mpif90
RUN=mpirun

isoth3d-mpi:
	${CC} -ffast-math -O3 -fopenmp -o isoth3d-mpi analysis.f90 isoth3d-mpi.f90 

isoth3d:
	gfortran -O3 -g -pg -fopenmp -o isoth3d isoth3d.f90 

runmpi: isoth3d-mpi
	${RUN} -np `egrep -o "procs([ ]?)=([ 0-9]*)" isoth3d-mpi.f90 | tr -d " " | cut -d"=" -f2` isoth3d-mpi

clean:
	rm -rf output-* isoth3d isoth3d2 gmon.out isoth3d-mpi analysis.mod
