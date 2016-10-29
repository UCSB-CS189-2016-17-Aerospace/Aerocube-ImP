#include "gtest/gtest.h"

TEST (SameNumberTest, PositiveNos) {
  EXPECT_EQ (18.0, 18);
  EXPECT_EQ (25.4, 25.4);
  EXPECT_NE (50.3321, 25);
}


int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
