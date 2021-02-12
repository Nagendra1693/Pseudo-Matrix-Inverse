# Pseudo-Matrix-Inverse

Since the matrix inverse is only possible for square matrices, there is a special way to calculate the inverse of a non-square matrix. The actual question of matrix inverse araises during the linear algebra calculations. A matrix inverse is a matrix which produces an identity matrix when it is multiplied by actual matrix. This is as follow:
A x A<sup>-1</sup> = I


If the columns of a matrix A are linearly independent, so  A<sup>T</sup>· A  is invertible and we obtain with the following formula the pseudo inverse:<br>
A<sup>+</sup> = (A<sup>T</sup> · A)<sup>-1</sup> · A<sup>T</sup>
<br>Here  A<sup>+</sup>  is a left inverse of  A , what means:  A<sup>+</sup>· A = I.  

However, if the rows of the matrix are linearly independent, we obtain the pseudo inverse with the formula:
<br>A<sup>+</sup> = A<sup>T</sup>· (A · A<sup>T</sup>)<sup>-1</sup><br>
This is a right inverse of  A , what means:  A · A<sup>+</sup> = I.
