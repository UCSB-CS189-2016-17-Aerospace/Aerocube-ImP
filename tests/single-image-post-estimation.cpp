#include "gtest/gtest.h"

TEST (SquareRootTest, PositiveNos) {
  EXPECT_EQ (18.0, square-root (324.0));
  EXPECT_EQ (25.4, square-root (646.16));
  EXPECT_EQ (50.3321, square-root(2533.310224));
}


int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
